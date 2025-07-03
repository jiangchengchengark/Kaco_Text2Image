from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
PROJECT_ROOT=os.path.dirname(os.path.abspath(__file__))
SAVE_DIR=os.path.join(PROJECT_ROOT,"static/images")
#读取config.yaml文件

################################################# 读取配置文件 #####################################
import yaml
with open(os.path.join(PROJECT_ROOT,"config.yaml"), 'r', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
LOCAL_URL_PREFIX="http://localhost:"+str(config["params"]["port"])
SEVER_URL=config["params"]['server_url']


################################################################################################
app = FastAPI()
# 确保目录存在
os.makedirs(SAVE_DIR, exist_ok=True)

# 将 static/images 挂载为 /images 路径
app.mount("/images", StaticFiles(directory="static/images"), name="images")

@app.get("/")
def index():
    return {"msg": "Image server is running."}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
