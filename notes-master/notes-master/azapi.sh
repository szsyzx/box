#!/bin/bash

sub_id=$(az account list --query [].id -o tsv)
az ad sp create-for-rbac --role contributor --scopes /subscriptions/$sub_id
