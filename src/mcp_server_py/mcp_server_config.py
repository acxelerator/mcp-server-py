from pydantic import BaseModel
import json


class McpServerConfig(BaseModel):
    name: str
    command: str
    args: list[str]

    @staticmethod
    def loads(name: str, data: dict) -> "McpServerConfig":
        return McpServerConfig(name=name, command=data["command"], args=data["args"])

    @staticmethod
    def load(path: str) -> list["McpServerConfig"]:
        result = []
        with open(path, mode="r") as f:
            data = json.load(f)
        for key, value in data["mcpServers"].item():
            result.append(McpServerConfig.loads(name=key, data=value))
        return result
