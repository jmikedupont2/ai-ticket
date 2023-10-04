from dockerbuild.baseimage import ExampleApplicationImage

import docker
from pathlib import Path
from docker.models.images import Image

class AITicketPoetryImage(ExampleApplicationImage):
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
        self.image_name: str = "h4ckermike/ai-ticket"
        self.dockerfile_directory: Path = Path(__file__).parent.parent.resolve()


class AutoGptImage(ExampleApplicationImage):
    def __init__(
        self,
        docker_client: docker.client,
        target_architecture: str,
        version: str,
    ):
        super().__init__(docker_client, target_architecture, version)
        self.image_name: str = "h4ckermike/act_base"
        self.dockerfile_directory: Path = (
            Path(__file__).parent.parent.resolve()
            / "vendor"
            / "act_base"
        )
class ActBaseImage(ExampleApplicationImage):
    def __init__(        self,        docker_client: docker.client,        target_architecture: str,        version: str,
    ):
        super().__init__(docker_client, target_architecture, version)
        self.image_name: str = "h4ckermike/autogpt"
        self.dockerfile_directory: Path = (
            Path(__file__).parent.parent.resolve()
            / "vendor"
            / "Auto-GPT/"
        )

class OpenAIImage(ExampleApplicationImage):
    def __init__(  self,  docker_client: docker.client,target_architecture: str,version: str ):
        super().__init__(docker_client, target_architecture, version)
        self.image_name: str = "h4ckermike/mockopenai"
        self.dockerfile_directory: Path = (
            Path(__file__).parent.parent.resolve()
            / "vendor"
            / "lollms/"
        )


