from pathlib import Path
from typing import Optional

import docker
from docker.models.images import Image

from dockerbuild.constants import (
    BASE_IMAGES,
    APPLICATION_SERVER_PORT,
)


class DockerImage:
    def __init__(
        self,
        docker_client: docker.client,
        target_architecture: str,
        version: str,
    ):
        self.docker_client: docker.client = docker_client
        self.dockerfile_name: str = "Dockerfile"
        self.dockerfile_directory: Optional[Path] = None
        self.image_name: Optional[str] = None
        self.image_tag: Optional[str] = None
        self.version: Optional[str] = version
        self.target_architecture: str = target_architecture


class AITicketPoetryImage(DockerImage):
    def __init__(
        self,
        docker_client: docker.client,
        target_architecture: str,
        version: str,
    ):
        super().__init__(docker_client, target_architecture, version)
        # An image name is made up of slash-separated name components,
        # optionally prefixed by a registry hostname.
        # see: https://docs.docker.com/engine/reference/commandline/tag/
        self.image_name: str = "h4ckermike/ai-ticket:test_ai_ticket"
        self.dockerfile_directory: Path = Path(__file__).parent.resolve()

    def build(self) -> Image:
        self.image_tag: str = f"{self.version}-{self.target_architecture}"

        buildargs: dict[str, str] = {
            "BASE_IMAGE": BASE_IMAGES[self.target_architecture],
            "APPLICATION_SERVER_PORT": APPLICATION_SERVER_PORT,
        }

        image: Image = self.docker_client.images.build(
            path=str(self.dockerfile_directory),
            dockerfile=self.dockerfile_name,
            tag=f"{self.image_name}:{self.image_tag}",
            buildargs=buildargs,
        )[0]
        return image


class ExampleApplicationImage(DockerImage):
    def build(
        self,
        target: str,
        base_image_tag: str,
    ) -> Image:
        self.image_tag = f"{self.version}-{self.target_architecture}"

        buildargs: dict[str, str] = {
            "BASE_IMAGE": base_image_tag,
        }
        image: Image = self.docker_client.images.build(
            path=str(self.dockerfile_directory),
            dockerfile=self.dockerfile_name,
            tag=f"{self.image_name}:{self.image_tag}",
            target=target,
            buildargs=buildargs,
        )[0]
        return image


class ActBaseImage(ExampleApplicationImage):
    def __init__(
        self,
        docker_client: docker.client,
        target_architecture: str,
        version: str,
    ):
        super().__init__(docker_client, target_architecture, version)
        # An image name is made up of slash-separated name components,
        # optionally prefixed by a registry hostname.
        # see: https://docs.docker.com/engine/reference/commandline/tag/
        self.image_name: str = "act_base"
        self.dockerfile_directory: Path = (
            Path(__file__).parent.parent.resolve()
            / "vendor"
            / "act_base"
        )


