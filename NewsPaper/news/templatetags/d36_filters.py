from django import template


register = template.Library()


@register.filter()
def censor(txt):

    replace_list = ['some', 'news-1']

    if not isinstance(txt, str):
        raise TypeError(f'invalid object type for censorship')

    else:
        for word in txt.split(" "):
            if word.lower() in replace_list:
                txt = txt.replace(word, f'{word[0]}{"*"*(len(word)-2)}{word[-1]}')
    return txt
