package com.puspo.demo.controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.puspo.demo.dto.PredictResponse;
import com.puspo.demo.dto.StudentRequest;
import com.puspo.demo.service.PredictService;

@RestController
@RequestMapping("/predict")
public class PredictController {
  private final PredictService predictService;

  PredictController(PredictService predictService) {
    this.predictService = predictService;
  }

  @PostMapping
  public PredictResponse prediction(@RequestBody StudentRequest request) {
    return predictService.predict(request);
  }
}
