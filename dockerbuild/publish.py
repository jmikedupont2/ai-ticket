import click
import docker

from docker.client import DockerClient

from dockerbuild.constants import (
    TARGET_ARCHITECTURES,
)
import dockerbuild.images
from dockerbuild.baseimage import BASE_IMAGE

@click.command()
@click.option(
    "--docker-hub-username",
    envvar="DOCKER_HUB_USERNAME",
    help="Docker Hub username",
)
@click.option(
    "--docker-hub-password",
    envvar="DOCKER_HUB_PASSWORD",
    help="Docker Hub password",
)
@click.option(
    "--version-tag", envvar="GIT_TAG_NAME", required=True, help="Version Tag"
)
@click.option("--registry", envvar="REGISTRY", help="Docker registry")
def main(
    docker_hub_username: str,
    docker_hub_password: str,
    version_tag: str,
    registry: str,
) -> None:
    docker_client: DockerClient = docker.from_env()    
    for target_architecture in TARGET_ARCHITECTURES:
        #import pdb
        #pdb.set_trace()
        for x in dir(dockerbuild.images) :
            cls = getattr(dockerbuild.images,x)
            if not isinstance(cls,type):
                continue
            print(cls)
            new_uvicorn_gunicorn_poetry_image = (cls(docker_client,target_architecture,version_tag))
            if new_uvicorn_gunicorn_poetry_image:
                for old_image in docker_client.images.list(new_uvicorn_gunicorn_poetry_image.image_name):
                    for tag in old_image.tags:
                        print("tag",tag)
                        docker_client.images.remove(tag, force=True)
                new_uvicorn_gunicorn_poetry_image.build(
                    target=target_architecture,base_image_tag=BASE_IMAGE
                )
        if docker_hub_username and docker_hub_password:
            login_kwargs: dict = {
                "username": docker_hub_username,
                "password": docker_hub_password,
            }
            if registry:
                login_kwargs["registry"] = registry
            docker_client.login(**login_kwargs)
        if registry:
            repository: str = (
                f"{registry}/{new_uvicorn_gunicorn_poetry_image.image_name}"
            )
        else:
            repository: str = new_uvicorn_gunicorn_poetry_image.image_name

        if False:
            for line in docker_client.images.push(
                repository,
                tag=new_uvicorn_gunicorn_poetry_image.image_tag,
                stream=True,
                decode=True,
            ):
                print(line)
                docker_client.close()


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()