from pathlib import Path
from typing import Optional

import docker
from docker.models.images import Image

from dockerbuild.constants import (
    BASE_IMAGES,
    APPLICATION_SERVER_PORT,
)

#
BASE_IMAGE="nikolaik/python-nodejs:python3.10-nodejs20"

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
        
    def build(self) -> Image:
        self.image_tag: str = f"{self.version}-{self.target_architecture}"
        buildargs: dict[str, str] = {
            "BASE_IMAGE": BASE_IMAGE,
            "APPLICATION_SERVER_PORT": APPLICATION_SERVER_PORT,        }
        image: Image = self.docker_client.images.build(
            path=str(self.dockerfile_directory),
            dockerfile=self.dockerfile_name,
            tag=f"{self.image_name}:{self.image_tag}",
            buildargs=buildargs,)[0]
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
        print("buildargs",dict(
            args=buildargs,                               
            path=str(self.dockerfile_directory),
            dockerfile=self.dockerfile_name,
            tag=f"{self.image_name}:{self.image_tag}",
            #target=target,
            buildargs=buildargs,
        ))
        
        image: Image = self.docker_client.images.build(
            
            path=str(self.dockerfile_directory),
            dockerfile=self.dockerfile_name,
            tag=f"{self.image_name}:{self.image_tag}",
            #target=target,
            buildargs=buildargs,
        )[0]
        return image
