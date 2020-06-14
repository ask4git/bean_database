"""
main.py
"""
# -*- coding: utf-8 -*-


class BeanDatabase(dict):
    def __init__(self):
        super().__init__()
        self.update({'country': '에티오피아'})
        self.update({'region': '구지 우라가'})
        self.update({'farm': '라로 보다'})
        self.update({'processing': '네츄럴'})
        self.update({'variety': 'Wolish and Dega'})
        self.update({'altitude': '1,974 ~ 2,280m'})
        self.update({'producer': 'SNAP Specialty Coffe'})

    def processing(self):
        while True:
            print('=========================')
            order = input('update : 1\nsearch : 2\nexit : 0\ninput? : ')

            try:
                if order == '1':
                    self.search_key()
                elif order == '2':
                    self.search_value()
                elif order == '0':
                    print('Bye!')
                    break
                else:
                    raise NotFoundOrder(order)
            except NotFoundKey as error:
                print(error)
            except NotFoundOrder as error:
                print(error)

    def search_key(self):
        """
        값을 업데이트
        """
        key_name = input('Value to update? : ')

        if self.key_validation_check(key_name):
            self.update_value(key_name)

    def search_value(self):
        """
        값을 검색
        """
        key_name = input('Value to print? : ')

        if self.key_validation_check(key_name):
            self.print_key(key_name)

    def update_value(self, key_name):
        value = input('Please input value : ')
        self.update({key_name: value})
        print('Update success!')

    def key_validation_check(self, key):
        """
        입력할 키가 존재하면 True, 없으면 False
        :return:
        """
        if key in self:
            return True
        else:
            raise NotFoundKey(key)

    def print_key(self, key_name):
        """
        값을 출력
        :return:
        """
        print(self.get(key_name))


class NotFoundKey(Exception):
    def __init__(self, key_name):
        self.key_name = key_name

    def __str__(self):
        return f'[NotFoundKey] {self.key_name} is not valid key'


class NotFoundOrder(Exception):
    def __init__(self, order):
        self.order = order

    def __str__(self):
        return f'[NotFoundOrder] {self.order} is not valid order'


def main():
    data = BeanDatabase()
    data.processing()


if __name__ == '__main__':
    main()
