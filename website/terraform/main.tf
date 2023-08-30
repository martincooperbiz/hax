provider "aws" {
  region = var.region
}

module "website" {
  source             = "tarekmulla/serverless-website/aws"
  version            = "1.0.0"
  app                = var.app
  region             = var.region
  tags               = var.tags
  domain             = var.domain
  alert_emails       = var.alert_emails
  images_path        = var.images_path
  website_files_path = var.website_files_path
}
