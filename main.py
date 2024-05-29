import replicate
from dotenv import load_dotenv

load_dotenv()

input = {
    "img": "https://i.pinimg.com/736x/da/fc/f0/dafcf05804f6920499de6b271777bcb3.jpg",
     "scale": 2,
    "version": "v1.4"
}

output = replicate.run(
    "tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c",
    input=input
)
print(output)
