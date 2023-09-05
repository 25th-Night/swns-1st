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
  env                       = "staging"
  lb_name                   = "be"
  subnet_netnum             = 1
  subnet_type               = "PUBLIC"
  db_name                   = "db"
  db_port_range             = "5432"
  db_init_script_path       = "db_init_script.tftpl"
  server_image_product_code = "SW.VSVR.OS.LNX64.UBNTU.SVR2004.B050"
}

data "ncloud_server_product" "product" {
  server_image_product_code = local.server_image_product_code

  filter {
    name   = "product_code"
    values = ["SSD"]
    regex  = true
  }

  filter {
    name   = "cpu_count"
    values = ["2"]
  }

  filter {
    name   = "memory_size"
    values = ["4GB"]
  }

  filter {
    name   = "base_block_storage_size"
    values = ["50GB"]
  }

  filter {
    name   = "product_type"
    values = ["HICPU"]
  }
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

module "db" {
  source           = "../../modules/server"
  ncp_access_key   = var.ncp_access_key
  ncp_secret_key   = var.ncp_secret_key
  name             = local.db_name
  env              = local.env
  vpc_id           = module.network.vpc_id
  subnet_id        = module.network.subnet_id
  port_range       = local.db_port_range
  init_script_path = local.db_init_script_path
  init_script_envs = {
    username          = var.username
    password          = var.password
    postgres_db       = var.postgres_db
    postgres_user     = var.postgres_user
    postgres_password = var.postgres_password
    postgres_port     = local.db_port_range
    postgres_volume   = var.postgres_volume
    db_container_name = var.db_container_name
  }
  server_image_product_code = local.server_image_product_code
  server_product_code       = data.ncloud_server_product.product.product_code
}

resource "ncloud_public_ip" "db_public_ip" {
  server_instance_no = module.db.server_instance_no
}
