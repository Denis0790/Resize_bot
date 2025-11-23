class AspectChecker:
    FORMATS = {
        "square": 1.0,  # 1:1
        "post": 3 / 4,
        "vk_post": 16 / 9,
    }

    def __init__(self, target_format: str, tolerance: float = 0.4): # tolerance - допустимое отклонение
        if target_format not in self.FORMATS:
            raise ValueError(f"Unknown format: {target_format}")

        self.target_ratio = self.FORMATS[target_format]
        self.tolerance = tolerance

    def need_remove_background(self, width: int, height: int) -> bool: # возвращает true если нужно удалить фон
        current_ratio = width / height
        diff = abs(current_ratio - self.target_ratio)
        return diff > self.tolerance
