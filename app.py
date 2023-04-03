import openai

input_file = input("要約したい対象のファイルのパス: ")
with open(input_file, encoding='utf-8') as f:
  text = f.read()

res = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a help assistant"},
    {"role": "user", "content": f"この文章を要約してください。「{text}」"},
    # {"role": "assistant", "content": "月が満ち欠けするのは、地球の自転と月の公転が相互作用することにより起こります。地球の重力が月を引っ張るため、月は地球に向かって落下しますが、同時に、月の運動エネルギーが働いて、地球を避けるように進路を変えます。この結果、月は常に地球に向かって引きつけられつつも、地球の周りをぐるぐる回ります。この運動が太陽光を反射する月の表面の見え方に影響するため、満月や新月、半月などの満ち欠け現象が起こるのです。"},
    # {"role": "user", "content": "もう少し簡潔に教えてください。"},
  ]
)
res_content = res["choices"][0]["message"]["content"]
print(res_content)

with open("output.txt", "w")as f:
  f.write(res_content)
