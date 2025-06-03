terraform {
  required_version = ">= 1.1.9"
}

provider "null" {
  # Provider null, on peut simuler des actions ou appeler des scripts
}

resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "echo 'Terraform resource applied!'"
  }
}
