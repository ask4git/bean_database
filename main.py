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
            print('=========================\n어떤 명령을 실행할까요?')
            order = input('update : 1\nsearch : 2\nexit : 0\ninput? : ')
            if order == '1':
                self.search_key()
            elif order == '2':
                self.search_value()
            elif order == '0':
                print('안녕히 가세용!')
                break
            else:
                print('다시 입력해주세요!')

    def search_key(self):
        """
        값을 업데이트
        :return:
        """
        key_name = input('어떤 값을 업데이트할까요? : ')

        if key_name in self:
            # key is valid
            self.update_value(key_name)
        else:
            print('키가 존재하지 않아요!')

    def update_value(self, key_name):
        value = input('값을 입력하세요. : ')
        self.update({key_name: value})
        print('업데이트 성공!')

    def search_value(self):
        """
        값을 검색
        :return:
        """
        key_name = input('어떤 값을 출력할까요? : ')
        if key_name in self:
            # key is valid
            print('출력값 : {}'.format(self.get(key_name)))
        else:
            print('키가 존재하지 않아요!')

    def key_validation_check(self):
        """
        입력할 키가 존재하면 True, 없으면 False
        :return:
        """
        pass

    def not_find_key_error(self):
        """
        키가 없을때 에러를 출력
        :return:
        """
        pass

    def print_key(self):
        """
        값을 출력
        :return:
        """
        pass


def main():
    data = BeanDatabase()
    data.processing()


if __name__ == '__main__':
    main()
