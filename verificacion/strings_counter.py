# coding=utf-8

import operator


class StringsCounter(object):
    def count_strings(self, text):
        word_counter = {}

        # Si es un string lo dividimos en un array de strings
        if type(text) is str:
            # Python3 str is already decoded
            # text = text.decode('unicode_escape').encode('ascii','ignore')
            text = text.split()

        # Poner todo el texto en minusculas
        text = list(map(str.lower, text))

        # Quitar simbolos de puntuacion y stopwords
        for i in range(len(text)):
            if not text[i].isdigit() and len(text[i])>1:
                text[i] = self.clear_punctiation_symbols(text[i])
                if len(text[i])<2:
                    text[i]=""
                else:
                    text[i] = self.clear_stopwords(text[i])
            else:
                text[i]=""


        set_text = set(text)

        #eliminamos elementos vacios
        if "" in set_text:
            set_text.remove("")
        # Contamos el numero de palabras repetidas y lo almacenamso en un diccionario

        for word in set_text:
            word_counter[word] = self.count_words(word, text)

        # Lo ordenamos el diccionario por el numero de veces que haya aparecido la palabra
        sorted_dic = sorted(word_counter.items(), key=operator.itemgetter(1), reverse=True)

        print (sorted_dic)
        print ("\nNumero de palabras: " + str(len(text)))
        print ("Numero de palabras diferentes: " + str(len(set_text)) + "\n")

        return sorted_dic

    def clear_stopwords(self, word):
        stopwords = set(['un', 'una', 'unas', 'unos', 'uno', 'sobre', 'todo', 'también', 'tras', 'otro', 'algún', 'alguno', 'alguna', 'algunos', 'algunas', 'ser', 'es', 'soy', 'eres', 'somos', 'sois', 'estoy', 'esta', 'estamos', 'estais', 'estan', 'como', 'en', 'para', 'atras', 'porque', 'por', 'qué', 'estado', 'estaba', 'ante', 'antes', 'siendo', 'ambos', 'pero', 'por', 'poder', 'puede', 'puedo', 'podemos', 'podeis', 'pueden', 'fui', 'fue', 'fuimos', 'fueron', 'hacer', 'hago', 'hace', 'hacemos', 'haceis', 'hacen', 'cada', 'fin', 'incluso', 'primero', 'desde', 'conseguir', 'consigo', 'consigue', 'consigues', 'conseguimos', 'consiguen', 'ir', 'voy', 'va', 'vamos', 'vais', 'van', 'vaya', 'gueno', 'ha', 'tener', 'tengo', 'tiene', 'tenemos', 'teneis', 'tienen', 'el', 'la', 'lo', 'las', 'los', 'su', 'aqui', 'mio', 'tuyo', 'ellos', 'ellas', 'nos', 'nosotros', 'vosotros', 'vosotras', 'si', 'dentro', 'solo', 'solamente', 'saber', 'sabes', 'sabe', 'sabemos', 'sabeis', 'saben', 'ultimo', 'largo', 'bastante', 'haces', 'muchos', 'aquellos', 'aquellas', 'sus', 'entonces', 'tiempo', 'verdad', 'verdadero', 'verdadera', 'cierto', 'ciertos', 'cierta', 'ciertas', 'intentar', 'intento', 'intenta', 'intentas', 'intentamos', 'intentais', 'intentan', 'dos', 'bajo', 'arriba', 'encima', 'usar', 'uso', 'usas', 'usa', 'usamos', 'usais', 'usan', 'emplear', 'empleo', 'empleas', 'emplean', 'ampleamos', 'empleais', 'valor', 'muy', 'era', 'eras', 'eramos', 'eran', 'modo', 'bien', 'cual', 'cuando', 'donde', 'mientras', 'quien', 'con', 'entre', 'sin', 'trabajo', 'trabajar', 'trabajas', 'trabaja', 'trabajamos', 'trabajais', 'trabajan', 'podria', 'podrias', 'podriamos', 'podrian', 'podriais', 'yo', 'aquel'])
        for x in stopwords:
            if x==word:
                word = ""
                break
        return word

    def clear_punctiation_symbols(self, word):
        punctuation_symbols = set(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','<','>','|', ])
        for x in punctuation_symbols:
            word = word.replace(x, "")
        return word

    def count_words(self ,word, text):
        cont = 0
        for i in range(len(text)):
            if word == text[i]:
                cont += 1
        return cont

    def print_solution(dic):
        print ("|      Words      | Count |")
        print ("---------------------------")
        for item in dic:
            space = 0
            for x in [ord(c) for c in item[0]]:
                if x > 128:
                    space = space + 1
            print("| " + item[0] + " " * (16 - len(item[0]) + space) +
                  "| " + str(item[1]) + " " * (6 - len(str(item[1]))) + "|")
        print ("\n")
