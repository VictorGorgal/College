from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

mario = np.array(Image.open('mario.png'))[:, :, :3]
(l, c, p) = mario.shape
print(mario.shape)
plt.imshow(mario)

# Crie uma função mirror, que recebe img (np.array), reverse_x (bool) e reverse_y (bool) e
# retorna uma nova imagem, onde caso reverse_EIXO seja verdadeiro, esta deve ser img espelhada
# em EIXO. Em seguida, teste sua função com uma imagem de sua escolha


# Escolha uma imagem qualquer e realize um cisalhamento nela, sendo os fatores de sua escolha

