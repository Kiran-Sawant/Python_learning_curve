class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{0}>'.format(name)
        self.end_tag = '</{0}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag} {0.contents} {0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC', '')
        self.end_tag = ''       #DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')    #body contents will be built up separatly
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)   #composition technique
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)

#_______Polymorphism through composition_______#
class HtmlDoc(object):
    """The HtmlDoc object has instance variables
        that are composed of other class objects,
        hence implimenting polymorhism through composition"""

    def __init__(self, title=None):

        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    #________Creatig HtmlDoc Object_________#
    my_page = HtmlDoc(title='generic title')
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This is a paragraph')

    #___________Writing to html file_____________#
    with open('test.html', mode='w') as test_file:
        my_page.display(file=test_file)
    my_page.display()