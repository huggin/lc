import "slices"

type Job struct {
	start  int
	end    int
	profit int
}

func jobScheduling(startTime []int, endTime []int, profit []int) int {
	n := len(profit)
	jobs := []Job{Job{0, 0, 0}}
	for i := 0; i < n; i++ {
		jobs = append(jobs, Job{startTime[i], endTime[i], profit[i]})
	}
	slices.SortFunc(jobs, func(a, b Job) int {
		if a.end < b.end || a.end == b.end && a.start < b.start {
			return -1
		}
		return 1
	})

	dp := make([]int, n+1)
	dp[0] = 0
	for i := 1; i <= n; i++ {
		j, _ := slices.BinarySearchFunc(jobs[0:i], jobs[i].start+1, func(a Job, t int) int {
			if a.end < t {
				return -1
			} else if a.end > t {
				return 1
			}
			return 0
		})
		dp[i] = max(dp[i-1], dp[j-1]+jobs[i].profit)
	}
	return dp[n]
}
