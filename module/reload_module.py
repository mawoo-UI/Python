# 모듈 재로딩
import importlib
import my_module

# 모듈을 수정한 후에는 재로딩 필요
print(f"Version before reloading: {my_module.version}")

# 업데이트된 모듈을 사용하려면 재로딩
my_module = importlib.reload(my_module)

print(f"Version after reloading: {my_module.version}")
print(f"Use new function: {my_module.subtract(10, 3)}")