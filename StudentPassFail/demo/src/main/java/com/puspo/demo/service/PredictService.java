package com.puspo.demo.service;

import com.puspo.demo.dto.PredictResponse;
import com.puspo.demo.dto.StudentRequest;

public interface PredictService {
  PredictResponse predict(StudentRequest request);
}
