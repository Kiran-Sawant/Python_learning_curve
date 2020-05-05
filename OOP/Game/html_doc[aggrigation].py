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

#_______Polymorphism through Aggrigation_______#
class HtmlDoc(object):
    """The HtmlDoc objects has instance variables
    that not defined as class objects, but clients can
    pass other class objects to it. hence implimenting 
    polymorhism through aggrigation"""

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    #_______creating class instances for creating a page_______#
    new_body = Body()
    new_body.add_tag('h1', 'Aggrigation Example')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggrigation uses existing instances"
                            "of objects to buildup objects.")
    new_body.add_tag('p', "The composed object doesn't own the object that it's composed of"
                            "- if it's destroyed, those objects continue to exist.")
    new_doctype = DocType()
    new_header = Head('Aggregation document')

    #______Creating as HtmlDoc object______#
    my_page = HtmlDoc(new_doctype, new_header, new_body)

    #________Writing to an html file________#
    with open('test2.html', mode='w') as test_doc:
        my_page.display(file=test_doc)