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
  region      = KR
  site        = public
  support_vpc = true
}

data "ncloud_vpc" "vpc" {
  id = var.vpc_id
}

resource "ncloud_login_key" "loginkey" {
  key_name = "${var.name}-key-${var.env}"
}

resource "ncloud_access_control_group" "acg" {
  name   = "${var.name}-acg-${var.env}"
  vpc_no = var.vpc_id
}

resource "ncloud_access_control_group_rule" "acg-rule" {
  access_control_group_no = ncloud_access_control_group.acg.id

  inbound {
    protocol    = "TCP"
    ip_block    = "0.0.0.0/0"
    port_range  = var.port_range
    description = "accept ${var.port_range} port for ${var.name}"
  }
}

resource "ncloud_init_script" "init" {
  name = "set-${var.name}-server-${var.env}"
  content = templatefile(
    "${path.module}/${var.init_script_path}",
    var.init_script_envs
  )
}
