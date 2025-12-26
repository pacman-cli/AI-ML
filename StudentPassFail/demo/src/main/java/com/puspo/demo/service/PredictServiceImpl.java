package com.puspo.demo.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.puspo.demo.dto.PredictResponse;
import com.puspo.demo.dto.StudentRequest;

@Service
public class PredictServiceImpl implements PredictService {
  // Create restTemplate object
  private final RestTemplate restTemplate = new RestTemplate();
  private static final String ML_API_URL = "http://127.0.0.1:5000/predict";

  public PredictResponse predict(StudentRequest request) {
    return restTemplate.postForObject(
        ML_API_URL,
        request,
        PredictResponse.class);
  }
}
