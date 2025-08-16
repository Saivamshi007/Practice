variable "lambda_name" {
  description = "Lambda function name"
  default     = "lambda_function"
}

variable "s3_bucket" {
  description = "S3 bucket where Lambda code zip is stored"
  default     = "lambdabucketforpractice"
}

variable "s3_key" {
  description = "Path to Lambda zip inside the bucket"
  default     = "lambda_function/lambda_function.zip"
}
