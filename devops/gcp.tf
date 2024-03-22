terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  credentials = file(var.credentials_file)
  project     = var.proyecto-gcp
  region      = var.region_gcp
  zone        = var.zone_gcp
}

resource "google_compute_instance" "default" {
  name         = "project0"
  machine_type = "f1-micro"
  zone         = var.zone_gcp

  boot_disk {
    initialize_params {
      image = "ubuntu-1804-bionic-v20200908"
    }
  }

  metadata_startup_script = "sudo apt-get update && sudo apt -y install python3-pip && sudo apt-get install -y git && git clone https://github.com/J48UFRIL/reto_final.git"

  network_interface {
    network = "default"
    access_config {}
  }

  tags = ["http-server", "https-server"]
}



resource "google_compute_firewall" "http-server" {
  name    = "default-allow-http"
  network = "default"

  allow {
    protocol = "tcp"
    ports = ["80", "8000", "8880", "22", "443", "5000"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags = ["http-server"]
}

resource "google_compute_firewall" "https-server" {
  name    = "default-allow-https"
  network = "default"

  allow {
    protocol = "tcp"
    ports = ["80", "8000", "8880", "22", "443", "5000"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags = ["https-server"]
}


output "ip" {
  value = google_compute_instance.default.network_interface.0.access_config.0.nat_ip
}