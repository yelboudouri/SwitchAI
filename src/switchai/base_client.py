from abc import ABC
from typing import Union, List, Optional, Generator

from PIL.Image import Image

from switchai.types import (
    ChatResponse,
    TranscriptionResponse,
    ImageGenerationResponse,
    ChatChoice,
    EmbeddingResponse,
)


class BaseClient(ABC):
    def chat(
        self,
        messages: List[str | ChatChoice | dict],
        temperature: Optional[float] = 1.0,
        max_tokens: Optional[int] = None,
        n: Optional[int] = 1,
        tools: Optional[List] = None,
        stream: Optional[bool] = False,
    ) -> Union[ChatResponse, Generator[ChatResponse, None, None]]:
        """
        Sends a chat request to the AI model and returns the response.

        Args:
            messages: A list of messages to send to the model.
            temperature: Sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic..
            max_tokens: The maximum number of tokens to generate. Defaults to None.
            n: How many chat completion choices to generate for each input message.
            tools: A list of tools the model may call.
            stream: Whether to stream the response.

        Returns:
            ChatResponse: The response from the model.
        """
        pass

    def embed(self, inputs: Union[str, Image, List[Union[str, Image]]]) -> EmbeddingResponse:
        """
        Embeds the input text using the AI model.

        Args:
            inputs: The input text to embed. Can be a single string or a list of strings.

        Returns:
            TextEmbeddingResponse: The response from the model.
        """
        pass

    def transcribe(self, audio_path: str, language: Optional[str] = None) -> TranscriptionResponse:
        """
        Convert speech to text.

        Args:
            audio_path: The path to the audio file.
            language: The language of the audio file.

        Returns:
            TranscriptionResponse: The response from the model.
        """
        pass

    def generate_image(self, prompt: str, n: Optional[int] = 1) -> ImageGenerationResponse:
        """
        Generate an image based on the provided prompt.

        Args:
            prompt: A text description of the desired image.
            n: The number of images to generate.

        Returns:
            ImageGenerationResponse: The response from the model.
        """
        pass
