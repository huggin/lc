import "math"

func poorPigs(buckets int, minutesToDie int, minutesToTest int) int {
	return int(math.Ceil(math.Log2(float64(buckets)) / math.Log2(float64(minutesToTest/minutesToDie)+1)))
}
