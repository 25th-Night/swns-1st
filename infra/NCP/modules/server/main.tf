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

data "ncloud_vpc" "vpc" {
  id = var.vpc_id
}

resource "ncloud_login_key" "loginkey" {
  key_name = "${var.name}-loginkey-${var.env}"
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

resource "ncloud_network_interface" "nic" {
  name      = "${var.name}-nic-${var.env}"
  subnet_no = var.subnet_id
  access_control_groups = [
    data.ncloud_vpc.vpc.default_access_control_group_no,
    ncloud_access_control_group.acg.access_control_group_no
  ]
}

resource "ncloud_init_script" "init" {
  name = "set-${var.name}-server-${var.env}"
  content = templatefile(
    "${path.module}/${var.init_script_path}",
    var.init_script_envs
  )
}

resource "ncloud_server" "server" {
  subnet_no                 = var.subnet_id
  name                      = "${var.name}-server-${var.env}"
  server_image_product_code = var.server_image_product_code
  server_product_code       = var.server_product_code
  login_key_name            = ncloud_login_key.loginkey.key_name
  init_script_no            = ncloud_init_script.init.init_script_no
  network_interface {
    network_interface_no = ncloud_network_interface.nic.network_interface_no
    order                = 0
  }
}
