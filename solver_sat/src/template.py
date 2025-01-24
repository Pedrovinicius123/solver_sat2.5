from dataclasses import dataclass

@dataclass
class Template:
    a: int
    b: int
    related: list

    def reversed_template(self):
        instance = self
        instance.a *= -1
        instance.b *= -1

        return instance

    def __eq__(self, other):
        assert isinstance(other, Template), f'{other} must be of Template instance'
        return (self.a == other.a and self.b == other.b) or (self.a == other.b and self.b == other.a)


class GeneralTemplate(Template):
    def __init__(self, a:int, b:int, sub_templates:list):
        super().__init__(abs(a), abs(b), sub_templates)

    def remove_template(self, temp: Template):
        if temp in self.related:
            self.related.remove(temp)

    def add_template(self, temp: Template):
        if temp not in self.related:
            self.related.append(temp)
