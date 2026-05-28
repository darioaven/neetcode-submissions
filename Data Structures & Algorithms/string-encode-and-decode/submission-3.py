class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "/empt"
        return "/enc".join(strs)


    def decode(self, s: str) -> List[str]:
        if s == "/empt":
            return []
        return s.split("/enc")