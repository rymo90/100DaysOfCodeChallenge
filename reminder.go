package main
import (
  "fmt"
  "time"
)
// func Remind(text string, t time.Duration )  {
//   fmt.Printf("klockan är %v: %v %v \n", t.Hour(),t.Minute(), text)
// }
func main()  {
  kl := time.Now()
  hour := kl.Hour()
  minute := kl.Minute()
  // fmt.Println(" ")
  fmt.Print(hour, ":", minute)
  // fmt.Println("klockan är ", time.Duration())
}
