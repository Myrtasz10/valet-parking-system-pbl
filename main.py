from parser_1 import Parser

if __name__ == '__main__':
    parser = Parser()
    parser.run()

    # Access the program parameters after the window is closed
    print(f'Number of parking spots: {parser.parking_spots}')
    print(f'Number of AGV shuttles: {parser.agv_shuttles}')
    print(f'Number of depots: {parser.depots}')
    print(f'Parking spot width: {parser.parking_spot_width}')
    print(f'Parking spot height: {parser.parking_spot_height}')
    print(f'AGV shuttles speed: {parser.speed}')