terraform {
  required_providers {
    ncloud = {
      source = "NaverCloudPlatform/ncloud"
    }
  }
  required_version = ">= 0.13"
}

provider "ncloud" {
  access_key  = var.ncp_access_key
  secret_key  = var.ncp_secret_key
  region      = "KR"
  site        = "public"
  support_vpc = true
}

locals {
  env           = "staging"
  lb_name       = "be"
  subnet_netnum = 1
  subnet_type   = "PUBLIC"
}

module "network" {
  source = "../../modules/network"

  ncp_access_key = var.ncp_access_key
  ncp_secret_key = var.ncp_secret_key
  name           = local.lb_name
  env            = local.env
  subnet_netnum  = local.subnet_netnum
  subnet_type    = local.subnet_type
}
