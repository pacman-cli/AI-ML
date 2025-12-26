package com.puspo.demo.dto;

import com.fasterxml.jackson.annotation.JsonProperty;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class StudentRequest {
  @JsonProperty("hours_studied")
  private int hoursStudied;

  @JsonProperty("attendance")
  private int attendance;
}
