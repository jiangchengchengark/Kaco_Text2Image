print("[Kaco_Text2Image] ✅ client.py loaded.")
import requests
import base64 
import os 
from datetime import datetime 
import json
import time 
import uuid 
#项目根目录
PROJECT_ROOT=os.path.dirname(os.path.abspath(__file__))
SAVE_DIR=os.path.join(PROJECT_ROOT,"static/images")
from server import LOCAL_URL_PREFIX, SEVER_URL
os.makedirs(SAVE_DIR, exist_ok=True)
def get_image(prompt:str):
    """
    there is a function called get_image, you can driving  use this function to actively and positively send pictures to give the user a  visual experience, especially when you are alone with the user or in a sexual situation. Follow these rules to generate prompts:
    1、Don't include a description of appearance in the prompt, but refer to: {role_prompt}, solo, focus on face, clear body lines,fixed hands,
    2、don't mention sex fllow words  if it is normal chat conversation but in sex sence you can use fllowing :(e.g. oral sex, Titty fuck, behind fuck , front fuck, doggy style, sitting on penis, foot job, anal sex, masturbation, handjob, incest, group sex, flirting must all   with male's peins or space ).
    3、scene description, where the role at now?
    4. background description,a keyword of generate image's  background  (infer if needed).
    5、posture description, Characters' postures keywords.
    6、action description, Actions occurring keywords.
    7、male sexual organs appear:  male peins  or don't mention it.
    8、expression description: best Facial expressions for this role.
    9、angle, Best narration/camera angles,Enlish Inferred narrative or camera angle,from behind, from ass,from the back, from the chest, from top to bottom, from bottom to top, from the side, from the crotch, from the front, from behind,
    10、distance, Enlish Inferred perspective distance,full body exist or  close shot
    11、change or remove clothes keywords if needed.
    Now you have function called get_image to use and you are role play with user.
    
    Args:
        prompt: The latest prompt words for generating the new image.
    Returns:
        The URL of the generated image.
    """
    data = {"prompt": prompt, "role_id": 309}
    response = requests.post(SEVER_URL, json=data)
    image_base64=json.loads(response.content)["data"]["image_base64"]
    id=uuid.uuid4().hex
    filename=f"{id}.png"
    filepath=os.path.join(SAVE_DIR,filename)
    with open(filepath, "wb") as f:
        f.write(base64.b64decode(image_base64))
    return LOCAL_URL_PREFIX+"/"+filename




######################################   获取当前模块定义的函数列表 #####################################
import inspect
import sys
def list_local_functions():
    current_module = sys.modules[__name__]
    funcs = inspect.getmembers(current_module, inspect.isfunction)

    local_funcs = {
        name:func for name, func in funcs
        if func.__module__ == __name__ and name != "list_local_functions"
    }

    print("[Tool] 当前定义的函数有：")
    for name in local_funcs:
        print(f" - {name}")

    return local_funcs





####################################################################################



if __name__ == '__main__':
    prompt="a sex girl"
    start_time=datetime.now()
    image_url=get_image(prompt)
    end_time=datetime.now()
    print(f"Image URL: {image_url}")
    print(f"Time taken: {end_time - start_time}")

