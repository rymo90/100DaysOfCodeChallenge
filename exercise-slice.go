package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
	yttreY := make([][]uint8, dy)
	for y := range yttreY {
		yttreY[y] = make([]uint8, dx)
		for x := range yttreY[y] {
			yttreY[y][x] = uint8((x ^ y) / 2)
		}
	}

	return yttreY
}
func main() {
	pic.Show(Pic)
}
