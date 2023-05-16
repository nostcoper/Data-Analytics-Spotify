import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Texto de ejemplo
texto = ['Amor', 'Amor', 'Amor', 'Amor', 'Musica', 'Musica', 'Musica', 'Musica', 'Perdón', 'Perdón', 'Generosidad']
texto = ' '.join(texto)

# Crear el objeto WordCloud
nube_palabras = WordCloud().generate(texto)

# Mostrar la nube de palabras utilizando matplotlib
plt.imshow(nube_palabras, interpolation='bilinear')
plt.axis('off')
plt.show()
