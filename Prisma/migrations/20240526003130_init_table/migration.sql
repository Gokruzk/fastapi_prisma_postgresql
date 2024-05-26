-- CreateTable
CREATE TABLE "users_" (
    "dni" TEXT NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "email" VARCHAR(50) NOT NULL,
    "password" VARCHAR(300) NOT NULL,

    CONSTRAINT "users__pkey" PRIMARY KEY ("dni")
);
