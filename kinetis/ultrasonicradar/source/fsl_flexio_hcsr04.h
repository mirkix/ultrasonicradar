/*
 * fsl_flexio_hcsr04.h
 *
 *  Created on: 29.06.2016
 *      Author: mirko
 */

#ifndef SOURCE_FSL_FLEXIO_HCSR04_H_
#define SOURCE_FSL_FLEXIO_HCSR04_H_

#include "pin_mux.h"
#include "fsl_flexio.h"

void FLEXIO_HCSR_Init(uint8_t echo);
uint16_t FLEXIO_HCSR_Ping(uint8_t echo, GPIO_Type *base, uint32_t pin);

#endif /* SOURCE_FSL_FLEXIO_HCSR04_H_ */
