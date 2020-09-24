'''
计数器
'''
def generate_count():
    container = [0]

    def add_one():
        container[0] +=1
        print(f'这是第{container[0]}次访问')

    return add_one

count = generate_count()
count()
count()
count()
