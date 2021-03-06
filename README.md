# Backend SPAMAway

## Table of contents
1. [Project Status](#project-status)
1. [Getting Started](#Getting-Started)
    1. [Requirements](#Requirements)
    1. [Installation](#installation)
    1. [Usage](#usage)

# Project Status

Mocked isspam endpoint.

# Getting Started

## Requirements

  * Docker
  * Docker compose

## Installation

  `docker-compose up`

## Usage

### Check if an sms is spam
  You can check sms message for spam by using `/isspam/` endpoint:

  ```
  POST /isspam/
  Content-Type: application/json
  body:
  {
    “content”: “abcd aaa aaasd”
  }

  Response
  Content-Type: application/json
  Code:
    * 200: successful operation
    * 400: invalid input
  body:
  {
    “spamPropability”: double  [0.0, 1.0]
  }
  ```

  **Example**
  ```
  curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"content":"to jest spam"}' \
    http://localhost:8000/isspam/
  ```
  
  ### Feedback
  You can send feedback by using below endpoint

  **Example**
  ```
  curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"content":"to jest spam", "isSpam":true}' \
    http://localhost:8000/isspam/feedback
  ```

  **Example**
  ```
  curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"content":"to nie jest spam", "isSpam":false}' \
    http://localhost:8000/isspam/feedback
  ```

  ### Get feedback smses
  You get all of the smses by using `/isspam/lastsms` endpoint:

  **Example**
  ```
  curl http://localhost:8000/isspam/lastsms/

  ```
