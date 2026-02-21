create database SSIS_Practice
use SSIS_Practice

CREATE TABLE Princesses(
	Princessname nvarchar(255),
	FeministRating nvarchar(255),
	FirstAppeared int,
	Vehicle nvarchar(255)
	)

CREATE TABLE WeirdStats(
	StoreName nvarchar(255) NULL,
	Statistic nvarchar(10) NULL,
	NumberPurchases int NULL,
	Amount decimal(12, 2) NULL
)
	select * from Princesses
	Select * from WeirdStats