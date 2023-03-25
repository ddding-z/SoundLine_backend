"""
调用 chatgpt api
需要修改代理port、api_key
"""
import requests


def chatUtil(prompt):
    api_key = "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"
    model = "text-davinci-002"
    # 修改代理port
    proxies = {'http': 'http://127.0.0.1:7080', 'https': 'https://127.0.0.1:7080'}
    url = f"https://api.openai.com/v1/engines/{model}/completions"

    response = requests.post(
        url,
        json={
            "prompt": prompt,
            "max_tokens": 1000,

        },
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        proxies=proxies
    )
    # print(response.json()['choices'][0]['text'])
    return response.json()['choices'][0]['text']


if __name__ == '__main__':
    prompt = "假设你现在是安永北京分部审计小组的一名实习生，请你用中文写一封邮件，向你的HR（也就是Ella " \
             "Zhang），来咨询一些关于离职的事项。你要搞清楚的事情有两件：1.入职协议上规定想要获得实习证明，员工的实际实习天数必须达到实习期的90%，那么这90%是如何计算的？2" \
             ".离职手续必须在实习期结束当天办理吗，可否晚几天办理？ "
    answer = chatUtil(prompt)
#
