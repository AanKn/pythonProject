stu_list = [['李李渊', 82], ['李李世⺠民', 7], ['侯君集', 5], ['李李靖', 58], ['魏征', 41],  ['房⽞玄龄', 64], ['杜如晦', 65], ['柴绍', 94],
            ['程知节', 45], ['尉迟恭', 94], ['秦琼', 54], ['⻓长孙⽆无忌', 85], ['李李存恭', 98], ['封德彝', 16], ['段志⽞玄', 44],
            ['刘 弘基', 18], ['徐世绩', 86], ['李李治', 19], ['武则天', 39], ['太平公主', 57], ['⻙韦后', 76], ['李李隆隆基', 95],
            ['杨⽟玉环', 33], ['王勃', 49], ['陈⼦子昂', 91], ['卢照邻', 70], ['杨炯', 81], ['王之涣', 82], ['安禄⼭山', 18],
            ['史思明', 9], ['张巡', 15], ['雷雷万 春', 72], ['李李⽩白', 61], ['⾼高⼒力力⼠士', 58], ['杜甫', 27], ['⽩白居易易', 5],
            ['王维', 14], ['孟浩然', 32], ['杜牧', 95], ['李李商隐', 34], ['郭⼦子仪', 53], ['张易易之', 39], ['张昌 宗', 61],
            ['来俊⾂臣', 8], ['杨国忠', 84], ['李李林林甫', 95], ['⾼高适', 100], ['王昌龄', 40], ['孙思邈', 46], ['⽞玄奘', 84],
            ['鉴真', 90], ['⾼高骈', 85], ['狄仁杰', 62], ['⻩黄 巢', 79], ['王仙芝', 16], ['⽂文成公主', 13], ['松赞⼲干布', 47],
            ['薛涛', 79], ['⻥鱼⽞玄 机', 16], ['贺知章', 20], ['李李泌泌', 17], ['韩愈', 100], ['柳柳宗元', 88],
            ['上官婉⼉儿 五 代⼗十国:朱温', 55], ['刘仁恭', 6], ['丁会', 26], ['李李克⽤用', 39], ['李李存勖', 11], ['葛从周', 25],
            ['王建', 13], ['刘知远', 95], ['⽯石敬瑭', 63], ['郭威', 28], ['柴 荣', 50], ['孟昶', 17], ['荆浩', 84], ['刘彟', 18],
            ['张及之', 45], ['杜宇', 73], ['⾼高季兴', 39], ['喻皓', 50], ['历真', 70], ['李李茂贞', 6], ['朱友珪', 7], ['朱友贞', 11],
            ['刘守光', 2]]
stu_list1 = [list(elem) for elem in sorted(dict(stu_list).items(), key=lambda k: (100-k[1], k[0]))]  # reverse并不能用
print('new_stu_list = [')


def format_output(a, b):
    print('\t[')
    for i in stu_list1:
        if a >= i[1] >= b:
            print('\t\t', i, ',', end='\n', sep='')
    print('\t],')


list(map(format_output, [100, 89, 79, 69, 59], [90, 80, 70, 60, 0]))  # 前面如果加print,则会输出函数返回值None的列表,没list不会输出
print(']')
