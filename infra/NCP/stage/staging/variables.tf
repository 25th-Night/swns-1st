variable "ncp_access_key" {
  type = string
}

variable "ncp_secret_key" {
  type = string
}

variable "username" {
  type      = string
  sensitive = true
}


variable "password" {
  type      = string
  sensitive = true
}


variable "postgres_db" {
  type = string
}


variable "postgres_user" {
  type      = string
  sensitive = true
}


variable "postgres_password" {
  type      = string
  sensitive = true
}


variable "postgres_volume" {
  type = string
}


variable "db_container_name" {
  type = string
}
