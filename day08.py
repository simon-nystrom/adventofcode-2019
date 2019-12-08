from utils.printing import printed

file = open("day08.txt")
puzzle_input = file.read()
file.close()

width = 25
height = 6
num_layers = len(puzzle_input) // (width * height)


@printed
def part1(puzzle_input):
    fewest_zeroes = width * height
    fewest_zero_layer_idx = 0
    layer_results = {}

    for layer_idx in range(num_layers):
        digit_cnt = {}
        for j in range(height):
            for k in range(width):
                digit = puzzle_input[k + j * width +
                                     layer_idx * width * height]
                if digit in digit_cnt:
                    digit_cnt[digit] += 1
                else:
                    digit_cnt[digit] = 1
        if digit_cnt['0'] < fewest_zeroes:
            fewest_zeroes = digit_cnt['0']
            fewest_zero_layer_idx = layer_idx
            layer_results[layer_idx] = digit_cnt['1'] * digit_cnt['2']
    return layer_results[fewest_zero_layer_idx]


@printed
def part2(puzzle_input):
    TRANSPARENT = '2'
    img = [TRANSPARENT] * width * height
    for layer_idx in range(num_layers):
        for j in range(height):
            for k in range(width):
                digit = puzzle_input[k + j * width +
                                     layer_idx * width * height]
                pixel = img[k + j * width]
                if pixel == TRANSPARENT:
                    img[k+j*width] = digit
    result = '\n'
    for i in range(height):
        m = ''
        for j in range(width):
            m += img[j + width*i]
        result += m + '\n'
    return result


part1(puzzle_input)
part2(puzzle_input)
