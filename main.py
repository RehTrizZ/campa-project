import cv2

class Gradient:
    def __init__(self, photo):
        self.dict: dict = self.loadGradientBar(photo)

    
    def loadGradientBar(self, photo) -> dict:
        # Prende la barra in basso, trasforma ogni valore HEX di colore in una corrispondente temperature
        # E la inserisci nel dizionario che sara composto da (HEX, valore in gradi)
        pass

class Pixel:
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class Photo:
    def __init__(self, filename):
        self.img = ""
        self.test(filename)

    def test(self, filename: str):
        self.img = cv2.imread("data/" + filename)
        cv2.imshow("Photo: " + filename, self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    photo = Photo("IR_0014.jpg")


# Fare dei limiti per evitare le scritte:
# Gradi, FLIR, gradient bar e "mirino"