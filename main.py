import arcade
import random

NUM_SHAPES = 100
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]


class Cercle:
    def __init__(self, x, y):
        # la position est determinee par le clic, les autres parametres sont aleatoires
        self.centre_x = x
        self.centre_y = y
        self.rayon = random.randint(10, 30)
        self.change_x = random.randint(-5, 5)
        self.change_y = random.randint(-5, 5)
        self.color = random.choice(COLORS)

    def update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y
        # assurer que le cercle reste dans l'ecran
        if self.centre_x < self.rayon or self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.centre_y < self.rayon or self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice 1")
        self.liste_formes = []

    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for _ in range(NUM_SHAPES):
            center_x = random.randint(30, SCREEN_WIDTH - 30)
            center_y = random.randint(30, SCREEN_HEIGHT - 30)
            self.liste_formes.append(Cercle(center_x, center_y))

    def on_draw(self):
        arcade.start_render()
        for forme in self.liste_formes:
            forme.update()
            forme.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
