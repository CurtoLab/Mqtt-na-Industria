void loop()
{
    // Piscar LED para indicar atividade
    digitalWrite(LED_PIN, HIGH);
    delay(100);
    digitalWrite(LED_PIN, LOW);

    sensors_event_t humidity, temp;
    aht.getEvent(&humidity, &temp); // populate temp and humidity objects with fresh data

    // Verificar se leitura foi bem-sucedida
    if (isnan(temp.temperature) || isnan(humidity.relative_humidity))
    {
        Serial.println("❌ Erro ao ler AHT10!");
        delay(2000);
        return;
    }

    // Exibir dados no Serial Monitor
    Serial.println("📊 === LEITURA SENSOR ===");
    Serial.print("🌡️  Temperatura: ");
    Serial.print(temp.temperature, 1);
    Serial.println("°C");

    Serial.print("💧 Umidade: ");
    Serial.print(humidity.relative_humidity, 1);
    Serial.println("%");

    // Calcular índice de calor
    float heatIndex = calculateHeatIndex(temp.temperature, humidity.relative_humidity);
    Serial.print("🔥 Sensação térmica: ");
    Serial.print(heatIndex, 1);
    Serial.println("°C");

    Serial.println("========================\n");

    // Aguardar próxima leitura
    delay(5000); // 5 segundos
}

// Função para calcular índice de calor
float calculateHeatIndex(float temp, float humidity)
{
    return temp + (0.33 * (humidity / 100.0 * 6.105 * exp((17.27 * temp) / (237.7 + temp)))) - 0.5;
}