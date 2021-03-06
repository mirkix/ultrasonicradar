#ifndef SOURCE_FSL_FLEXIO_WS2812_H_
#define SOURCE_FSL_FLEXIO_WS2812_H_

#include <stdint.h>

#define FLEXIO_WS2812_BUFFER_SIZE 25

struct FLEXIO_WS2812_LED {
	uint8_t r;
	uint8_t g;
	uint8_t b;
};

void FLEXIO_WS2812_SendByte(uint8_t byte);
void FLEXIO_WS2812_Init();
void FLEXIO_WS2812_TransmitBuffer();
void FLEXIO_WS2812_Update(const struct FLEXIO_WS2812_LED *led);

#endif /* SOURCE_FSL_FLEXIO_WS2812_H_ */
