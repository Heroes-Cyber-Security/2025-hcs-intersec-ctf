flower_bouquet = {
  "A": "Rose ",
  "B": "Camellia ",
  "C": "Magnolia ",
  "D": "Poppy ",
  "E": "Tulip ",
  "F": "Chrysanthemum ",
  "G": "Hyacinth ",
  "H": "Violet ",
  "I": "Lavender ",
  "J": "Heather ",
  "K": "Petunia ",
  "L": "Gladiolus ",
  "M": "Yarrow ",
  "N": "Wisteria ",
  "O": "Hibiscus ",
  "P": "Edelweiss ",
  "Q": "Iris ",
  "R": "Anemone ",
  "S": "Kalmia ",
  "T": "Zinnia ",
  "U": "Lotus ",
  "V": "Oleander ",
  "W": "Begonia ",
  "X": "Foxglove ",
  "Y": "Sunflower ",
  "Z": "Dahlia ",

  "a": "Jasmine ",
  "b": "Freesia ",
  "c": "Bluebell ",
  "d": "Aconite ",
  "e": "Orchid ",
  "f": "Azalea ",
  "g": "Carnation ",
  "h": "Ursinia ",
  "i": "Gardenia ",
  "j": "Snowdrop ",
  "k": "Marigold ",
  "l": "Nerine ",
  "m": "Aster ",
  "n": "Xeranthemum ",
  "o": "Peony ",
  "p": "Daisy ",
  "q": "Buttercup ",
  "r": "Primula ",
  "s": "Crocus ",
  "t": "Verbena ",
  "u": "Snapdragon ",
  "v": "Cosmos ",
  "w": "Delphinium ",
  "x": "Fuchsia ",
  "y": "Primrose ",
  "z": "Scabiosa ",

  "0": "Hydrangea ",
  "1": "Amaranth ",
  "2": "Clematis ",
  "3": "Pansy ",
  "4": "Daffodil ",
  "5": "Lilac ",
  "6": "Calla ",
  "7": "Phlox ",
  "8": "Geranium ",
  "9": "Amaryllis ",
  "{": "Canna ",
  "}": "Silene ",
  "_": "Thistle ",
  "+": "Lotuswort ",
  "\\": "Anthurium ",
  "'": "Viola ",
  " ": "Cyclamen ",
  ":": "Ixora "
}

bouquet_flower = {bouquet: seed for seed, bouquet in flower_bouquet.items()}

def build_bouquet(seed_line):
  return "".join(flower_bouquet[seed] for seed in seed_line)

def disassemble_bouquet(arrangement):
  stems = arrangement.split(" ")
  return "".join(bouquet_flower[bouquet + " "] for bouquet in stems if bouquet)

def main():
  # flag = "A special bouquet for a special someone: HCS{c'est_la_vie_en_rose}"

  # print(build_bouquet(flag))

  special_bouquet = "Rose Cyclamen Crocus Daisy Orchid Bluebell Gardenia Jasmine Nerine Cyclamen Freesia Peony Snapdragon Buttercup Snapdragon Orchid Verbena Cyclamen Azalea Peony Primula Cyclamen Jasmine Cyclamen Crocus Daisy Orchid Bluebell Gardenia Jasmine Nerine Cyclamen Crocus Peony Aster Orchid Peony Xeranthemum Orchid Ixora Cyclamen Violet Magnolia Kalmia Canna Bluebell Viola Orchid Crocus Verbena Thistle Nerine Jasmine Thistle Cosmos Gardenia Orchid Thistle Orchid Xeranthemum Thistle Primula Peony Crocus Orchid Silene"

  print(disassemble_bouquet(special_bouquet))

if __name__ == "__main__":
  main()