class Worklist:
    def __init__(self):
        self.works = []
        self.completion = []
        self.not_completion = []
        self.no = []

    def write_work(self):
        while True:
            work = input("할 일을 입력하세요 입력 완료시 enter: ")
            self.works.append(work)
            if work == '':
                del self.works[-1]
                break
        return self.works

    def check_work(self):
        print(self.__str__())
        for index, x in enumerate(self.works):
            print(f'{index + 1} {x}')

        completionwork = input("완료할 일에 번호를 입력하세요 : ")

        for x in range(len(self.works)):
            if x == int(completionwork)-1:
                self.completion.append(self.works[x])
            else:
                self.not_completion.append(self.works[x])

            self.no = list(set(self.not_completion) - set(self.completion))



        print(f'완료한 일 : {set(self.completion)}')
        print(f'아직 완료하지 못한 일 : {set(self.no)}')

    def add_work(self):
        addition = input("추가할 일을 입력하세요 : ")
        self.works.append(addition)
        print(self.works)

    def del_work(self):
        print(self.__str__())
        for index, work in enumerate(self.works):
            print(f'{index + 1} {work}')
        deletion = input("삭제할 일에 번호를 입력하세요 : ")
        del self.works[int(deletion)-1]
        print(self.__str__())

    def __str__(self):
        return f' <오늘의 할 일>\n{self.works}'
